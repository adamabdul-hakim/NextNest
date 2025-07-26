import jwt
import os
from flask import request, jsonify

SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")

def verify_request():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None, jsonify({"error": "Unauthorized"}), 401

    # Extract token
    token = auth_header.split(" ")[1]

    try:
        # Decode and verify JWT with Supabase JWT secret
        payload = jwt.decode(
            token,
            SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        return payload, None, None
    except jwt.InvalidTokenError as e:
        print("JWT decode error:", e)
        return None, jsonify({"error": "Invalid token"}), 401

