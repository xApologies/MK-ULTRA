class AIError(Exception): pass
class InterpretationError(AIError): pass
class RootAuthorityError(InterpretationError): pass
class PolicyError(AIError): pass
class CollapseValidationError(AIError): pass
class ExternalModuleError(AIError): pass
