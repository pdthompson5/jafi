


Program → Expression*


Expression → FunctionDeclaration

FunctionDeclaration → “def” Identifier parameters “{” Expression  “}” | VariableDeclaration

VariableDeclaration → “set” identifier “=” expression | If

If → “if”  expression  “then”  expression (”else” expression)? | FunctionCall

InfixFunctionCall → “‘” (expression variable expression) | FunctionCall

FunctionCall  → variable (“(” (expression “,”)* expression “)”) * 

Variable → primary | identifier 

primary → Lambda | Number | String  | Bool | None | Char | Grouping 

Lambda →”\” ((identifier “,”)* identifier)? “:” expression 

Bool → “True” | “False”

Grouping → “(” expression “)”