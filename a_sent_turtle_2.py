class Message:
    """
        A Message class. Allows users to save the message details.
    """
    def __init__(self, message_id: int, message_title: str, message_body: str, sender: str):
        self.id = message_id
        self.title = message_title
        self.body = message_body
        self.sender = sender
        self.was_read = False

    def __str__(self) -> str:
        """
            The function returns a string containing the message and its details.
            :return: A string containing the message and its details.
        """
        return 'Message #' + str(self.id) + ', from ' + self.sender + '. ' +\
               self.title + ': ' + self.body

    def __len__(self) -> int:
        """
            The function returns the length of the message body.
            :return: The length of the message body.
        """
        return len(self.body)


class PostOffice:
    """A Post Office class. Allows users to message each other.
    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.
    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title, message_body, urgent=False):
        """Send a message to a recipient.
        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param str message_title: The title of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        new_message = Message(self.message_id, message_title, message_body, sender)
        if urgent:
            user_box.insert(0, new_message)
        else:
            user_box.append(new_message)
        return self.message_id

    def read_inbox(self, username: str, number_of_messages: int = -1) -> list:
        """
            The function receives a username and a desired number of messages (called N),
            the function returns the first N unread messages,
            from the message box of the user whose name was sent to the function.
            If there are less than N unread messages in the box,
            the function returns the existing messages.
            :param username: The user whose messages will be read.
            :param number_of_messages: The number of messages you want to read.
            :return: List of messages to read.
        """
        messages_to_be_read = []
        for message in self.boxes[username]:
            if number_of_messages == 0:
                return messages_to_be_read
            if not message.was_read:
                messages_to_be_read.append(message)
                message.was_read = True
                number_of_messages -= 1
        return messages_to_be_read

    def search_inbox(self, username: str, string_to_search: str) -> list:
        """
            The function gets a username and a string.
            It returns a list containing all the messages that contain the string, in their title or body.
            :param username: The user whose messages will be searched at.
            :param string_to_search: The string that will be searched in the messages.
            :return: A list of messages that in their title or body the string was found.
        """
        return [message for message in self.boxes[username]
                if string_to_search in message['title'] or string_to_search in message['body']]
