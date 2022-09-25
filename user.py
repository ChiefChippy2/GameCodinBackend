from dataclasses import dataclass, asdict


@dataclass
class User:
    username: str
    email: str

    @property
    def dict(self):
        return asdict(self)
