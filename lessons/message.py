"""Class to store a message"""

class Email:

    to: str
    message: str
    important: bool
    
    def __init__(self, recipient: str, message_text: str = "", importance_flag: bool = False):
        """Constructor of an email."""
        self.to = recipient
        self.message = message_text
        self.important = importance_flag

    def __str__(self) -> str:
        m_string: str = f"To: {self.to} \n"
        m_string += f"Important? {self.important}\n"
        m_string += f'"{self.message}"'
        return m_string
    
    def __mul__(self, factor: int): 
        self.message *= factor

email_to_chiara: Email = Email("chiara", "You are soooooo bad! Netflix and chill?", False)
print(email_to_chiara)
email_to_lauren: Email = Email("lauren", "Great job!")
print(email_to_lauren)