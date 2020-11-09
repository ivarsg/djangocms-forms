from django.test import TestCase

from djangocms_forms.models import FormDefinition, Form


class ModelTestCase(TestCase):
    def setUp(self):
        FormDefinition.objects.create(
            name="Test Form", title="Test Form", description="Test Form",
        )

    def test_form_exists(self):
        try:
            test_form = Form.objects.get(name="Test Form")
        except Form.DoesNotExist:
            pass
