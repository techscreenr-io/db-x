from datetime import datetime, timezone

from elasticsearch_dsl import (
    Boolean,
    Date,
    Document,
    Integer,
    Keyword,
    Nested,
    Text,
)


class BusinessDoc(Document):
    _created_at = Date()
    _updated_at = Date()

    uuid = Keyword()
    business_name = Text(fields={"keyword": Keyword()})
    contact_name = Text(fields={"keyword": Keyword()})
    services = Text(multi=True)
    location = Keyword(multi=True)
    email = Text(fields={"keyword": Keyword()}, multi=True)
    twitter_handle = Text(fields={"keyword": Keyword()}, multi=True)
    whatsapp_link = Keyword()
    website = Text()

    def save(self, skip_empty=False, **kwargs):
        if not self._created_at:
            self._created_at = datetime.now(timezone.utc)

        self._updated_at = datetime.now(timezone.utc)

        return super().save(skip_empty=skip_empty, **kwargs)
