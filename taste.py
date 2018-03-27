from exactonline.storage import IniStorage

class MyIniStorage(IniStorage):
    def get_response_url(self):
        "Configure your custom response URL."
        return self.get_base_url() + '/oauth/success/'

storage = MyIniStorage('/config.ini')
