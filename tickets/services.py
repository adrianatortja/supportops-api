def categorize_ticket(message):
    message = message.lower()

    shipping_keywords = ['shipping', 'delivery', 'track', 'tracking', 'order status', 'where is my order']
    refund_keywords = ['refund', 'return', 'money back', 'damaged', 'cancel']
    technical_keywords = ['error', 'bug', 'not working', 'broken', 'login issue', 'payment failed']

    if any(keyword in message for keyword in refund_keywords):
        return 'refund'

    if any(keyword in message for keyword in shipping_keywords):
        return 'shipping'

    if any(keyword in message for keyword in technical_keywords):
        return 'technical'

    return 'general'


def detect_priority(message):
    message = message.lower()

    high_priority_keywords = ['urgent', 'angry', 'complaint', 'escalate', 'chargeback', 'fraud']
    medium_priority_keywords = ['refund', 'return', 'damaged', 'late', 'delay', 'not working']

    if any(keyword in message for keyword in high_priority_keywords):
        return 'high'

    if any(keyword in message for keyword in medium_priority_keywords):
        return 'medium'

    return 'low'


def generate_suggested_reply(category):
    replies = {
        'refund': 'We are sorry to hear about the issue with your order. We will review the details and help you with the refund process.',
        'shipping': 'Thanks for reaching out. We will check the shipping status of your order and provide an update as soon as possible.',
        'technical': 'Thanks for reporting this issue. Our team will review the technical problem and help you resolve it.',
        'general': 'Thanks for contacting us. We will review your request and get back to you as soon as possible.',
    }

    return replies.get(category, replies['general'])
