"""
Django admin command to send verification approved email to learners
"""

import logging

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from verify_student.utils import send_verification_approved_email

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    This command sends email to learner for which the Software Secure Photo Verification has approved

    Example usage:
        $ ./manage.py lms send_verification_approved_email --username=staff
    """
    help = 'Send email to users for which Software Secure Photo Verification has expired'

    def add_arguments(self, parser):
        parser.add_argument('--username', help="The learner's email address or integer ID.")

    def handle(self, *args, **options):
        """
        Handler for the command

        It creates batches of expired Software Secure Photo Verification and sends it to send_verification_expiry_email
        that used edx_ace to send email to these learners
        """
        username = options['username']
        logger.info('1. Trying to send ID verification approved email to user: {}'.format(username))
        user = User.objects.get(username=username)

        email_was_successful = send_verification_approved_email(user)
        logger.info('2. Email sending to user: {}, success: {}'.format(username, email_was_successful))
