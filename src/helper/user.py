# Create a function to hash a user ID
def hash_user_id(user_id: str) -> str:
    return str(uuid.uuid5(uuid.uuid1(), user_id)).replace("-", "")

# Define a function to hash an API key
def hash_api_key(api_key: str) -> str:
    return pwd_context.hash(api_key)

# Define a function to create a new API key
def create_api_key():
    return str(uuid4())

# Define a function to generate an access token for an API key
def create_access_token(api_key: str):
    expire = datetime.utcnow() + timedelta(seconds=API_KEY_EXPIRATION_TIME)
    to_encode = {"api_key": api_key, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, API_KEY_SECRET_KEY, algorithm=API_KEY_ALGORITHM)
    return encoded_jwt