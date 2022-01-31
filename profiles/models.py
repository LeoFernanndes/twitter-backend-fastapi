from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from services.database_connection import Base


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    id_str = Column(String(255), unique=True)
    name = Column(String(255), unique=False)
    screen_name = Column(String(255), unique=False)
    location = Column(String(255), unique=False)
    profile_location = Column(String(255), unique=False)
    description = Column(String(255), unique=False)
    url = Column(String(255), unique=False)
    protected = Column(String(255), unique=False)
    followers_count = Column(Integer, unique=False)
    listed_count = Column(Integer, unique=False)
    created_at = Column(String(255), unique=False)
    favourites_count = Column(Integer, unique=False)
    time_zone = Column(String(255), unique=False)
    geo_enabled = Column(String(255), unique=False)
    verified = Column(String(255), unique=False)
    statuses_count = Column(Integer, unique=False)
    lang = Column(String(255), unique=False)


# class Tweet(Base):
#     __tablename__ = "tweet"

#     id = Column(Integer, primary_key=True, index=True)
#     id_str = Column(String(255), unique=True)
#     user_screen_name = Column(String(255), unique=False)
#     user_id_str = Column(String(255), unique=False)
#     full_text = Column(Text, unique=False)
#     truncated = Column(String(255), unique=False)
#     created_at = Column(String(255), unique=False)
#     entities_hashtags = Column(String(255), unique=False)
#     entities_symbols = Column(String(255), unique=False)
#     entities_user_mentions = Column(String(255), unique=False)
#     entities_urls = Column(String(255), unique=False)
#     geo = Column(String(255), unique=False)
#     coordinates = Column(String(255), unique=False)
#     place = Column(String(255), unique=False)
#     contributors = Column(String(255), unique=False)
#     is_quote_status = Column(String(255), unique=False)
#     favorite_count = Column(Integer, unique=False)
#     favorited = Column(String(255), unique=False)
#     retweeted = Column(String(255), unique=False)
#     possibly_sensitive = Column(String(255), unique=False)
#     lang = Column(String(255), unique=False)
