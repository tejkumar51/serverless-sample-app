import testutils
from unittest import TestCase


class Test(TestCase):

    @classmethod
    def setup_class(cls):
        print('\r\nSetting up the class')
        testutils.create_lambda('handler_lambda')
        testutils.create_bucket('sample_bucket')
        testutils.create_dynamo('sample_table')

    #@classmethod
    def teardown_class(cls):
        print('\r\nTearing down the class')
        testutils.delete_lambda('handler_lambda')
        testutils.delete_bucket('sample_bucket')

    def test_that_two_objects_in_s3_after_two_invocations(self):
        _ = testutils.invoke_function_and_get_message('sample-service-local-hello')
        bucket_objects = testutils.list_s3_bucket_objects('sample_bucket')
        self.assertEqual(len(bucket_objects), 2)