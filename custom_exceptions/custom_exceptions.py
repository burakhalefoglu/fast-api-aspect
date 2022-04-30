class ValidationException(Exception):
    """Exception raised for errors in the input valdation.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message={"message": "Kullanıcı istek bilgileri doğrulanırken hata oluştu.",
                                "status": False,
                                "data": None}):
        self.message = message
        super().__init__(self.message)


class UnauthorizedAccessException(Exception):
    """Exception raised for errors in the token valdation.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message={"message": "Bu işlemi yapabilmek için giriş yapmalısınız!",
                                "status": False,
                                "data": None}):
        self.message = message
        super().__init__(self.message)


class SecurityException(Exception):
    """Exception raised for errors in the autorize valdation.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message={"message": "Bu işlemi yapabilmek için yetkiniz bulunmamaktadır!",
                                "status": False,
                                "data": None}):
        self.message = message
        super().__init__(self.message)
