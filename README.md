# Salesforce AI Prompts 🚀

A community-driven library of ready-to-use AI prompts for Salesforce development — validation rules, formula fields, Apex classes, Flows, LWC, and more.

Copy a prompt, fill in your context, paste it into your favorite AI assistant (Claude, ChatGPT, Copilot, etc.), and get consistent, best-practice-aligned output every time.

## Why this exists

Every developer writes prompts differently, which means inconsistent quality and repeated effort. This repo standardizes prompts by Salesforce component type so any developer can:

- Grab a battle-tested prompt instead of writing one from scratch
- Get output that follows Salesforce best practices (bulkification, governor limits, naming conventions)
- Contribute improvements back so the whole community benefits

## How to use

1. Browse `/prompts` and find the folder matching your component type (e.g. `validation-rules`, `apex`, `flows`)
2. Open the `.md` file for your use case
3. Fill in the **Context** section with your object, field, and requirement details
4. Paste the full prompt into your AI tool of choice
5. Review the output — always validate against your org's specific config before deploying

## Folder structure

```
prompts/
├── apex/              Trigger handlers, batch/queueable/schedulable classes, REST integrations, test classes
├── validation-rules/  Conditional required fields, date validations, cross-object rules
├── formula-fields/    Text, date/time, cross-object, nested-IF formulas
├── custom-fields/     Field creation specs, picklists, naming conventions
├── flows/             Record-triggered, screen, scheduled flows, error handling
├── lwc/                Component scaffolding, wire adapters, Apex calls, Jest tests
├── metadata/           Custom metadata types, custom permissions, permission sets
├── integration/        Named credentials, platform events, callouts
├── security/           Sharing rules, field-level security reviews
└── documentation/       Technical design docs, release notes
```

## Contributing

Want to add a prompt or improve an existing one? See [CONTRIBUTING.md](CONTRIBUTING.md).

Every prompt follows the same template — see [`templates/_prompt-template.md`](templates/_prompt-template.md) — so contributions stay consistent and easy to review.

## License

See [LICENSE](LICENSE).
