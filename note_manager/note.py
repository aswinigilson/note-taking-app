from datetime import datetime


class Note:
    def __init__(self, title, content, tags, timestamp=None):
        self.title = title
        self.content = content
        self.tags = tags
        self.timestamp = timestamp or datetime.now().isoformat()

    def save(self):
        return {
            "title": self.title,
            "content": self.content,
            "tags": self.tags,
            "timestamp": self.timestamp
        }

    def display(self):
        print(f"Title: {self.title}")
        print()
        print(f"Timestamp: {self.timestamp}")
        print()
        print(f"Tags: {', '.join(self.tags)}")
        print()
        print(f"Content: {self.content}")
        print()
        print("-" * 27)

    def matches_search(self, term):
        term = term.lower()

        return (
            term in self.title.lower()
            or term in self.content.lower()
            or any(term in tag.lower() for tag in self.tags)
        )