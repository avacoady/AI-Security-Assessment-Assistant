# Access Advisor — Preliminary assessment

**Draft — human review required.** Custom IAM checklist; not a compliance certification.

Run mode: deterministic demo (no AI). Documentation support does not verify operating effectiveness.

## Executive summary

The assessment records 2 documented gaps, 1 unverified controls, and 1 supported controls.

Prioritize confirmation of documented gaps. Obtain missing evidence before deciding whether unverified controls require remediation. Suggested priorities and owners are provisional.

## Multifactor authentication

**Status:** documented_gap · **Priority:** High

Optional MFA leaves remote access dependent on passwords.

**Evidence:**
- access-policy.md, line 2 [cabce571ee7e43dd]: MFA is optional for remote access.

**Proposed next step:** Confirm and enforce MFA for remote and privileged access; track exceptions.

**Follow-up:** Provide MFA enforcement settings and an exception register.

## Administrator access

**Status:** documented_gap · **Priority:** High

Shared administrator access weakens individual accountability.

**Evidence:**
- access-policy.md, line 3 [7568735f69a4095b]: IT staff share one administrator account.

**Proposed next step:** Use individually assigned admin accounts and review least privilege.

**Follow-up:** Provide a privileged-account inventory and ownership records.

## Employee offboarding

**Status:** supported · **Priority:** Triage pending

The written process assigns responsibilities and a deadline. Execution has not been verified.

**Evidence:**
- access-policy.md, line 4 [ab72f6fca893b4f3]: HR notifies IT before departure; IT disables accounts by the end of the final working day.

**Proposed next step:** Provide a recent completed offboarding ticket and account-disable timestamps.

**Follow-up:** Provide a recent completed offboarding ticket and account-disable timestamps.

## Periodic access reviews

**Status:** unverified · **Priority:** Triage pending

The evidence does not establish whether access reviews occur.

**Evidence:**
- evidence-register.txt, line 1 [b3b3f4f5a1bc2a20]: Access-review documentation was not supplied.

**Proposed next step:** Who reviews access, how often, and can you supply the latest completed review?

**Follow-up:** Who reviews access, how often, and can you supply the latest completed review?

