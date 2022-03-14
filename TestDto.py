from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class TestDto:
    a: Optional[int] = None
    b: Optional[str] = None
    c: Optional[str] = None
