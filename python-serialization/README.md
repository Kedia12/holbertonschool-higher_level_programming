Serialization, Deserialization, and Marshaling (with Python examples)

When software needs to store data, send it over a network, or share it between programs, it must convert in-memory objects into a format that can travel outside the current process. Three closely related terms often appear:

* Serialization
* Deserialization
* Marshaling (and its reverse, unmarshaling)

Serialization

Serialization converts an in-memory object into a storable/transmittable representation—usually bytes (binary) or text (like JSON).

JSON serialization (text)

import json

data = {
    "name": "Ada",
    "age": 42,
    "skills": ["python", "math"],
    "active": True,
    "meta": None,
}

json_text = json.dumps(data, indent=2)
print(json_text)

Pickle serialization (binary, Python-only)

import pickle

data = {"x": [1, 2, 3], "y": ("a", "b")}

blob = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
print(type(blob), len(blob))  # <class 'bytes'> ...

Deserialization

Deserialization is the reverse: it turns the serialized representation (bytes/text) back into a usable in-memory object.

JSON deserialization

import json

json_text = '{"name": "Ada", "age": 42}'
obj = json.loads(json_text)

print(obj)         # {'name': 'Ada', 'age': 42}
print(type(obj))   # <class 'dict'>

Pickle deserialization (⚠️ trusted data only)

import pickle

blob = pickle.dumps({"a": 1})
obj = pickle.loads(blob)

print(obj)  # {'a': 1}

⚠️ Security note: Never pickle.loads() / pickle.load() data from untrusted sources. Pickle can execute arbitrary code during loading.

Marshaling

Marshaling usually means preparing data to cross a boundary (process, machine, language, RPC call).

It often includes serialization, but may also include:

* Converting non-supported types into transferable representations (type mapping)
* Packaging metadata (message type, version, schema id, etc.)
* Ensuring compatibility across environments

In short: marshaling = serialization + boundary-crossing concerns.

Example: Marshaling a custom object into JSON-friendly data

JSON can’t serialize datetime or custom classes by default, so we marshal them into a standard representation.

import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone

@dataclass
class User:
    name: str
    created_at: datetime

u = User(name="Ada", created_at=datetime.now(timezone.utc))

def marshal_user(user: User) -> dict:
    d = asdict(user)
    d["created_at"] = user.created_at.isoformat()  # datetime -> string
    return d

payload = marshal_user(u)
json_text = json.dumps(payload, indent=2)
print(json_text)

Reverse direction: Unmarshaling (reconstructing types)

from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    name: str
    created_at: datetime

def unmarshal_user(d: dict) -> User:
    return User(
        name=d["name"],
        created_at=datetime.fromisoformat(d["created_at"])  # string -> datetime
    )

incoming = {"name": "Ada", "created_at": "2026-02-10T12:34:56+00:00"}
u2 = unmarshal_user(incoming)
print(u2)
print(type(u2.created_at))

Differences (the short, accurate way)

Serialization vs Deserialization

* Serialization: object → bytes/text
* Deserialization: bytes/text → object

Marshaling vs Serialization

* Serialization: focuses on encoding an object into a portable format.
* Marshaling: focuses on preparing data to cross boundaries, which may involve:
    * converting types (e.g., datetime → string),
    * adding metadata,
    * packaging requests/responses for protocols (HTTP/RPC/etc.).

Mini “RPC-style” marshaling example (packaging metadata + args)

This shows marshaling as “build a message to send” (method name + args + version), then serialize it:

import json
from datetime import datetime, timezone

def marshal_rpc_call(method: str, args: dict) -> str:
    # marshal: add metadata + normalize tricky types
    safe_args = dict(args)
    if isinstance(safe_args.get("timestamp"), datetime):
        safe_args["timestamp"] = safe_args["timestamp"].isoformat()

    message = {
        "version": 1,
        "method": method,
        "args": safe_args,
    }
    # serialize for transport
    return json.dumps(message)

wire = marshal_rpc_call(
    "create_user",
    {"name": "Ada", "timestamp": datetime.now(timezone.utc)}
)

print(wire)  # send over network
Unmarshal on the receiving side:
import json
from datetime import datetime

def unmarshal_rpc_call(wire: str) -> dict:
    message = json.loads(wire)  # deserialize
    args = message["args"]

    # unmarshal: reconstruct types if desired
    if "timestamp" in args:
        args["timestamp"] = datetime.fromisoformat(args["timestamp"])

    return message

msg = unmarshal_rpc_call(wire)
print(msg["method"], msg["args"])
print(type(msg["args"]["timestamp"]))