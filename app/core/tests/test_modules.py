from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """이메일 신규유저 생성 테스트"""
        email = "test@seoulappdev.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """신규유저 이메일 정규화"""
        email = "test@SEOULAPPDEV.COM"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invaild_email(self):
        """이메일 없는 신규유저 생성 에러 테스트"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """신규관리자 생성 테스트"""
        user = get_user_model().objects.create_superuser(
            "test@seoulappdev.com",
            "test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
