from urllib.parse import quote

import msal
import requests


class GraphMailer:
    def __init__(self, tenant_id: str, client_id: str, client_secret: str, sender: str) -> None:
        self.sender = sender
        self.client = msal.ConfidentialClientApplication(
            client_id=client_id,
            authority=f"https://login.microsoftonline.com/{tenant_id}",
            client_credential=client_secret,
        )

    def send(self, recipient: str, subject: str, body: str) -> None:
        token_result = self.client.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
        access_token = token_result.get("access_token")
        if not access_token:
            raise RuntimeError(f"Microsoft identity token request failed: {token_result.get('error_description', 'unknown error')}")

        response = requests.post(
            f"https://graph.microsoft.com/v1.0/users/{quote(self.sender, safe='')}/sendMail",
            headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
            json={
                "message": {
                    "subject": subject,
                    "body": {"contentType": "Text", "content": body},
                    "toRecipients": [{"emailAddress": {"address": recipient}}],
                },
                "saveToSentItems": True,
            },
            timeout=30,
        )
        if not response.ok:
            raise RuntimeError(f"Microsoft Graph sendMail failed ({response.status_code}): {response.text}")