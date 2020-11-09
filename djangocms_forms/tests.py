from django.test import TestCase

from djangocms_forms.models import FormDefinition


class ModelTestCase(TestCase):
    def setUp(self):
        FormDefinition.objects.create(
            name="Test Form",
            title="Test Form",
            description="Test Form",
        )
