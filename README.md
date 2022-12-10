# pipedream-assemblyai

# Pipedream <> Assembly AI
This repository provides a simple example of how to configure Pipedream to call Assembly AI. These scripts can be used to accept a call recording as an input, and then send that call recording to Assembly AI for things like transcription, sentiment analysis, and classification.

## Basic Setup
- Setup a Pipedream account at https://www.pipedream.com
- Create an account at Assembly API and get an API key

### Webhook Setup
- Create two workflows in Pipedream
- The first workflow will accept the call recordings via webhook and send it to Assembly AI (you can use any other input method here) - Name this something like "Receive call recording"
- The second workflow will receive the results from Assembly AI and then make them available for processing. This workflow will also start with a webhook.

### Script setup
- In the first workflow, first setup the webhook, then create a Python task and copy the contents of receive_call.py into this step.
- In the second workflow, first setup the webook, then create a Python task and copy the contents of receive_assembly.py into this step.

