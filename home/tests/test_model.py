from unittest import TestCase

from home.models import Conversation


class ConvModelTest(TestCase):
    def test_model_creation(self):
        count_before_test = Conversation.objects.all().count()
        Conversation.objects.create(
            ask="이름이 뭐니?",
            answer="심심이야"
        )
        count_after_test = Conversation.objects.all().count()

        self.assertEquals(1, count_after_test - count_before_test)
