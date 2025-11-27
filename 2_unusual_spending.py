import pytest

class EmailService:
    def send(self, to):
        pass

class UnusualSpendingActivityDetector():
    def __init__(self, emailService, paymentRepository):
        self.emailService = emailService
        self.paymentRepository = paymentRepository

    def computeTotalPayementByCategory(self, allPayments):
        totalPayementByCategory = {}

        for (amount, category) in allPayments:
            if category not in totalPayementByCategory:
                totalPayementByCategory[category] = 0

            totalPayementByCategory[category] += amount

        return totalPayementByCategory

    def __getUnusualSpendingActivity(self, currentMonthPaymentByCategory, previousMonthPaymentByCategory):
        unusualSpendingActivityDetector = []

        for paymentCategory in currentMonthPaymentByCategory:
            totalCurrentMonthPayment = currentMonthPaymentByCategory[paymentCategory]
            totalPreviousMonthPayment = 0

            if paymentCategory in previousMonthPaymentByCategory:
                totalPreviousMonthPayment = previousMonthPaymentByCategory[paymentCategory]

            if totalCurrentMonthPayment > totalPreviousMonthPayment * 1.5:
                unusualSpendingActivityDetector.append((paymentCategory, totalCurrentMonthPayment))

        return unusualSpendingActivityDetector

    def __formatEmail(self, unusualSpendingActivityDetector):
        return ", ".join([ str(x[0]) + " " + str(x[1]) for x in unusualSpendingActivityDetector])

    def detect(self, userId):
        currentMonthPayment = self.paymentRepository.get_payments_for_current_month(userId)
        previousMonthPayment = self.paymentRepository.get_payments_for_previous_month(userId)

        currentMonthPaymentByCategory = self.computeTotalPayementByCategory(currentMonthPayment)
        previousMonthPaymentByCategory = self.computeTotalPayementByCategory(previousMonthPayment)

        unusualSpendingActivity = self.__getUnusualSpendingActivity(currentMonthPaymentByCategory, previousMonthPaymentByCategory)

        if len(unusualSpendingActivity) > 0:
            self.emailService.send(self.__formatEmail(unusualSpendingActivity))

        pass

def test_given_no_payment_for_user_then_no_email_send(mocker):
    emailServiceSpy = mocker.Mock()
    emailServiceSpy.send.return_value = None

    paymentRepository = mocker.Mock()
    paymentRepository.get_payments_for_current_month.return_value = []
    paymentRepository.get_payments_for_previous_month.return_value = []
    unusualSpendingActivityDetector = UnusualSpendingActivityDetector(emailServiceSpy, paymentRepository)

    unusualSpendingActivityDetector.detect(1)

    assert emailServiceSpy.call_count == 0

caseDeltaSupTo50Percent = [
    ([ (500, "Loisir") ], [ ], "Loisir 500"),
    ([ (200, "Loisir"), (300, "Loisir") ], [ (100, "Loisir"),(100, "Loisir") ], "Loisir 500"),
    ([ (230, "Loisir"), (80, "Nourriture")], [(150, "Loisir"), (50, "Nourriture")], "Loisir 230, Nourriture 80")
]

@pytest.mark.parametrize("currentMonthHistory, previousMonthHistory, expectedEmail", caseDeltaSupTo50Percent)
def test_given_a_payment_loisir500_and_no_previous_payment_for_user_then_email_send(mocker, currentMonthHistory, previousMonthHistory, expectedEmail):
    emailServiceSpy = mocker.Mock()
    emailServiceSpy.send.return_value = None

    paymentRepository = mocker.Mock()
    paymentRepository.get_payments_for_current_month.return_value = currentMonthHistory
    paymentRepository.get_payments_for_previous_month.return_value = previousMonthHistory
    unusualSpendingActivityDetector = UnusualSpendingActivityDetector(emailServiceSpy, paymentRepository)

    unusualSpendingActivityDetector.detect(1)

    emailServiceSpy.send.assert_called_once_with(expectedEmail)

caseNoDeltaSupTo50Percent = [
    ([ (500, "Loisir") ], [ (400, "Loisir") ]),
    ([ (200, "Loisir"), (300, "Loisir") ], [ (300, "Loisir"),(100, "Loisir") ]),
    ([ (225, "Loisir"), (75, "Nourriture")], [(150, "Loisir"), (50, "Nourriture")]),
]

@pytest.mark.parametrize("currentMonthHistory,previousMonthHistory", caseNoDeltaSupTo50Percent)
def test_given_a_payment_loisir500_and_loisir400_previous_payment_for_user_then_no_email(mocker, currentMonthHistory, previousMonthHistory):
    userId = 1
    emailServiceSpy = mocker.Mock()
    emailServiceSpy.send.return_value = None

    paymentRepository = mocker.Mock()
    paymentRepository.get_payments_for_current_month.return_value = currentMonthHistory
    paymentRepository.get_payments_for_previous_month.return_value = previousMonthHistory
    unusualSpendingActivityDetector = UnusualSpendingActivityDetector(emailServiceSpy, paymentRepository)

    unusualSpendingActivityDetector.detect(userId)

    paymentRepository.get_payments_for_current_month.assert_called_once_with(userId)
    assert emailServiceSpy.send.call_count == 0
