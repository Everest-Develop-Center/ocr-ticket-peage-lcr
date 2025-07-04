from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

AUTHORIZED_TOKENS = ["bWKoGqmjDBy9UPmJ2dtD7a97X4i6lbYrFecsE2GCMuLFMKLiGABbIO8KEiQ1Gey6"]

class HTTPBearerCustom(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        print("je suis ici..")
        if not credentials or credentials.scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="⚠️ Accès interdit : aucun token Bearer fourni ou format invalide"
            )
        return credentials



security = HTTPBearerCustom()

def token_checking(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    print("token used", token)
    if token not in AUTHORIZED_TOKENS:
        raise HTTPException(status_code=401, detail="Invalid token")


