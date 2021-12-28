class TestPlugin:
    """Offline tests"""

    def test_filter(self, mocker, requests_mock):
        requests_mock.post(_getdefault(mocker.bot, "server"), text="test1")

        msg = mocker.get_one_reply(filename="file.txt")
        assert "test1" in msg.text

        # bot should only upload files sent in private
        msgs = mocker.get_replies(filename="file.txt", group="TestGroup")
        assert not msgs

        # there is no file, message should be ignored
        msgs = mocker.get_replies(text="hello")
        assert not msgs
