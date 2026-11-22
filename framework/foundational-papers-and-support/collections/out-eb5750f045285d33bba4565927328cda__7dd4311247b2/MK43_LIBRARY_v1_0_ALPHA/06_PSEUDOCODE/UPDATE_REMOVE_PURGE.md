# Update, Remove, and Purge Pseudocode

FUNCTION REPLACE_ADDRESS(handle,new_package): validate; insert new version; switch active pointer atomically; preserve prior version; rebuild indexes; receipt.

FUNCTION REMOVE_ADDRESS(handle): resolve active; calculate impact; require allowed; mark inactive; remove active indexes; commit; receipt.

FUNCTION PURGE_ADDRESS(handle,reason,cascade_policy): resolve any; compute complete deletion set and dependent impact; require allowed; delete recoverable content, aliases, relations, membership, versions, object; validate remaining Library; commit; rebuild; emit purge receipt with former hash and impact only.
