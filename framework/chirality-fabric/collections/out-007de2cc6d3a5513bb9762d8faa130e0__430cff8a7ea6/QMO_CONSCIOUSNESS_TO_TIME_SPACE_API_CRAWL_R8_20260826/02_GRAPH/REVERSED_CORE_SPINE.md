# Reverse-rooted core dependency view

> IMPORTANT: arrows below indicate reverse traversal/read order. Source dependency direction is preserved in the machine ledger; inverse relation names are not promoted as source mathematics.

`@consciousness`  ←[incoming source dependency from `@cosmology`; relations: COMPOSED_DEPENDENCY, CONNECTS_TO, DEPENDS_TO, DIRECTED_TO, EXPLICIT_ARROW, FORMALLY_DEPENDS_ON, RECOVERED_DEPENDENCY, USED_BY, VERTICAL_CHAIN]—  `@cosmology`
`@cosmology`  ←[incoming source dependency from `@black_hole_cosmology`; relations: COMPOSED_DEPENDENCY, CONNECTS, DEPENDS_ON, FAMILY_DEPENDS_ON]—  `@black_hole_cosmology`
`@black_hole_cosmology`  ←[incoming source dependency from `@black_hole`; relations: BLACK_HOLE_GLOBAL_REACHES, BLACK_HOLE_MODEL_REACHES]—  `@black_hole`
`@black_hole`  ←[incoming source dependency from `@spacetime`; relations: BLACK_HOLE_CROSS_FAMILY_NODE, COMPOSED_DEPENDENCY, FEEDS_BLACK_HOLE_MODEL, GLOBALLY_FEEDS_BLACK_HOLE, SUPPORTS]—  `@spacetime`
`@spacetime`  ←[incoming source dependency from `@time_shell`; relations: COMPOSED_DEPENDENCY]—  `@time_shell`
`@time_shell`  ←[incoming source dependency from `@graviton`; relations: COMPOSED_DEPENDENCY, DEPENDS_TO, DIRECTED_TO, EXPLICIT_ARROW, FORMALLY_DEPENDS_ON, RECOVERED_DEPENDENCY, USED_BY]—  `@graviton`
`@graviton`  ←[incoming source dependency from `@helicon`; relations: COMPOSED_DEPENDENCY, DEPENDS_TO, DIRECTED_TO, EXPLICIT_ARROW, FORMALLY_DEPENDS_ON, INLINE_CHAIN, RECOVERED_DEPENDENCY, USED_BY, VERTICAL_CHAIN]—  `@helicon`
`@helicon`  ←[incoming source dependency from `@chirality`; relations: COMPOSED_DEPENDENCY]—  `@chirality`
`@chirality`  ←[incoming source dependency from `@persistence`; relations: DEPENDS_TO, DIRECTED_TO, EXPLICIT_ARROW, FORMALLY_DEPENDS_ON, RECOVERED_DEPENDENCY, USED_BY]—  `@persistence`
`@persistence`  ←[incoming source dependency from `@bandwidth`; relations: COMPOSED_DEPENDENCY, DEPENDS_TO, DIRECTED_TO, EXPLICIT_ARROW, FORMALLY_DEPENDS_ON, RECOVERED_DEPENDENCY, USED_BY]—  `@bandwidth`
`@bandwidth`  ←[incoming source dependency from `@resolution`; relations: COMPOSED_DEPENDENCY, DEPENDS_TO, DIRECTED_TO, EXPLICIT_ARROW, FORMALLY_DEPENDS_ON, RECOVERED_DEPENDENCY, USED_BY]—  `@resolution`
`@resolution`  ←[incoming source dependency from `@genesis_field`; relations: COMPOSED_DEPENDENCY, DEPENDS_TO, DIRECTED_TO, EXPLICIT_ARROW, FORMALLY_DEPENDS_ON, HAS_RESOLUTION_COORDINATE, RECOVERED_DEPENDENCY, USED_BY, VERTICAL_CHAIN]—  `@genesis_field`
`@genesis_field`  ←[incoming source dependency from `@time_space`; relations: COMPOSED_DEPENDENCY, DEPENDS_TO, DIRECTED_TO, EXPLICIT_ARROW, FORMALLY_DEPENDS_ON, RECOVERED_DEPENDENCY, USED_BY]—  `@time_space`
