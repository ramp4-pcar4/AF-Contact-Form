# R4MP Marketing Site Contact Form

<p>This is the Azure Function that handles email submissions through our marketing site contact form.</p>

## Set up

<p>Create a Postmark template and add its ID along with your API key to the Configuration panel with the names: </p>

```
POSTMARK_TEMPLATE_ID
POSTMARK_API_TOKEN
```

<p>Simply deploy your Azure Function using the extension available in VS Code, or configure your function to build and deploy whenever changes are made to your repo.</p>
