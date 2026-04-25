# Runtime Fixes

## 1.5.2

Fixed:

```text
ReferenceError: async is not defined
```

Cause:

A generated patch left a standalone `async` token before a normal function declaration. Browsers interpreted it as a variable reference instead of an async function keyword.

Resolution:

- Removed the standalone token.
- Kept the function as a normal synchronous function.
- Revalidated JavaScript syntax.
