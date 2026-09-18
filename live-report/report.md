# Access Advisor — Preliminary assessment

**Draft — human review required.** Custom IAM checklist; not a compliance certification.

Run mode: AI via Ollama (cloud-backed). Documentation support does not verify operating effectiveness.

## Executive summary

The assessment records 2 documented gaps, 1 unverified controls, and 1 supported controls.

Prioritize confirmation of documented gaps. Obtain missing evidence before deciding whether unverified controls require remediation. Suggested priorities and owners are provisional.

## Multifactor authentication

**Status:** documented_gap · **Priority:** High

Optional MFA for remote access increases the risk of unauthorized access via credential theft.

**Evidence:**
- access-policy.md, line 2 [cabce571ee7e43dd]: MFA is optional for remote access.

**Proposed next step:** Confirm and enforce MFA for remote and privileged access; track exceptions.

**Follow-up:** Is there a technical configuration that enforces MFA for specific high-risk remote access paths?

## Administrator access

**Status:** documented_gap · **Priority:** High

Shared administrator accounts prevent individual accountability and increase the risk of unauthorized changes.

**Evidence:**
- access-policy.md, line 3 [7568735f69a4095b]: IT staff share one administrator account.

**Proposed next step:** Use individually assigned admin accounts and review least privilege.

**Follow-up:** Can the organization provide a list of individual admin accounts currently in use?

## Employee offboarding

**Status:** supported · **Priority:** Triage pending

The policy defines a process for timely account removal with HR as the trigger and IT as the owner.

**Evidence:**
- access-policy.md, line 4 [ab72f6fca893b4f3]: HR notifies IT before departure; IT disables accounts by the end of the final working day.

**Proposed next step:** Can you provide a sample of offboarding tickets showing the time between HR notification and account disablement?

**Follow-up:** Can you provide a sample of offboarding tickets showing the time between HR notification and account disablement?

## Periodic access reviews

**Status:** unverified · **Priority:** Triage pending

No documentation or responses were provided regarding the performance of periodic access reviews.

**Evidence:**
- evidence-register.txt, line 1 [b3b3f4f5a1bc2a20]: Access-review documentation was not supplied.
- questionnaire.csv, line 2 [1c59cbd72c4a41ac]: access reviews,Awaiting response from the system owners

**Proposed next step:** Please provide the most recent access review logs and the policy defining the review frequency.

**Follow-up:** Please provide the most recent access review logs and the policy defining the review frequency.

