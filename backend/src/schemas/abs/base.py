from datetime import datetime, date

from pydantic import BaseModel, ConfigDict

class BaseCreate(BaseModel):
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_encoders={
                                                datetime: lambda v: v.isoformat(),
                                                date: lambda v: v.isoformat()
                                            })
    
class BaseUpdate(BaseModel):
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_encoders={
                                                datetime: lambda v: v.isoformat(),
                                                date: lambda v: v.isoformat()
                                            })
    
class BaseRead(BaseModel):
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_encoders={
                                                datetime: lambda v: v.isoformat(),
                                                date: lambda v: v.isoformat()
                                            })