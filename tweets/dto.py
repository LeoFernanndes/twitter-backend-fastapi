from pydantic import BaseModel
from typing import Union

class TweetDto(BaseModel):
    id:int
    id_str:Union[str, None]
    user_screen_name:Union[str, None]
    user_id_str:Union[str, None]
    full_text:Union[str, None]
    truncated:Union[str, None]
    created_at:Union[str, None]
    entities_hashtags:Union[str, None]
    entities_symbols:Union[str, None]
    entities_user_mentions:Union[str, None]
    entities_urls:Union[str, None]
    geo:Union[str, None]
    coordinates:Union[str, None]
    place:Union[str, None]
    contributors:Union[str, None]
    is_quote_status:Union[str, None]
    favorite_count:int
    favorited:Union[str, None]
    retweeted:Union[str, None]
    possibly_sensitive:Union[str, None]
    lang:Union[str, None]

    class Config:
        orm_mode = True
