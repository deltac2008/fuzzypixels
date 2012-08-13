import gdata.auth
import gdata.docs.service
key="56174940938-kfsjgiqa1jq8rn8ouesc5c1f9dmfqmag.apps.googleusercontent.com"
secret="LRe2ZGtHnTKj_0vmyJrqyviw"
client=gdata.docs.service.DocsService()
client.SetOAuthInputParameters(gdata.auth.OAuthSignatureMethod.HMAC_SHA1,key,consumer_secret=secret)
token=client.FetchOAuthRequestToken(scopes="https://docs.google.com/feeds/ ", extra_parameters={'oauth_version':'2.0'})
client.SetOAuthToken(token)
auth_url=client.GenerateOAuthAuthorizationURL()
import webbrowser
webbrowser.open(auth_url)
# wait for key press otherwise auth fails because we continue too soon

client.UpgradeToOAuthAccessToken()
client.current_token
dfeed=client.GetDocumentListFeed()
dfeed.entry[0].title
