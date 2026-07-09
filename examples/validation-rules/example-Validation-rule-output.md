# Example Output – Validation Rule (Contact)

This is a sample output generated from `/prompts/apex/trigger-handler.md`, using this filled-in context:

- Object: Opportunity
- Events: after update
- Logic: When Stage changes to "Closed Won", update the related Account's `Last_Won_Date__c` field
- Existing automation: none

## Files produced

**OpportunityTrigger.trigger**
```apex
trigger OpportunityTrigger on Opportunity (after update) {
    OpportunityTriggerHandler.handle(Trigger.new, Trigger.oldMap);
}
```

**OpportunityTriggerHandler.cls** (excerpt)
```apex
public with sharing class OpportunityTriggerHandler {
    public static void handle(List<Opportunity> newList, Map<Id, Opportunity> oldMap) {
        Set<Id> accountIdsToUpdate = new Set<Id>();

        for (Opportunity opp : newList) {
            Opportunity oldOpp = oldMap.get(opp.Id);
            if (opp.StageName == 'Closed Won' && oldOpp.StageName != 'Closed Won') {
                accountIdsToUpdate.add(opp.AccountId);
            }
        }

        if (!accountIdsToUpdate.isEmpty()) {
            List<Account> accountsToUpdate = new List<Account>();
            for (Id accId : accountIdsToUpdate) {
                accountsToUpdate.add(new Account(Id = accId, Last_Won_Date__c = Date.today()));
            }
            update accountsToUpdate;
        }
    }
}
```

This is a trimmed illustrative example — real output will include full test classes and fault-tolerant bulk handling. Use this file as a reference for the expected shape of output, not as production-ready code.
