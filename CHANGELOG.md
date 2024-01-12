# CHANGELOG



## v0.0.2 (2024-01-12)

### Chore

* chore: update ci ([`80e4db2`](https://github.com/Atticuszz/fastapi_supabase_template/commit/80e4db23f17662b3f7e21ae10624712dfc989a59))

### Fix

* fix: fix pytest bug of failed test gotrue client in trio,
feat: add crud test ([`0d22fb1`](https://github.com/Atticuszz/fastapi_supabase_template/commit/0d22fb1fd833d815d29e141a913a36e07d7cabdc))

### Unknown

* Merge pull request #8 from Atticuszz/release

release ([`6e9b807`](https://github.com/Atticuszz/fastapi_supabase_template/commit/6e9b8074f7f8c7112dee1b8ee1864a6f1c061d36))

* bugs: failed to auth as dep on new user by access token ([`cba0fbd`](https://github.com/Atticuszz/fastapi_supabase_template/commit/cba0fbdb71c98ddb63545ecbc619bd8d29ffff20))

* Merge branch &#39;main&#39; of github.com:/Atticuszz/fastapi_supabase_template ([`59d9d45`](https://github.com/Atticuszz/fastapi_supabase_template/commit/59d9d45ae449fd6f48fc1d16f1f063b4feea361e))


## v0.0.1 (2024-01-11)

### Chore

* chore(release): bump version to v0.0.1 ([`4ee5548`](https://github.com/Atticuszz/fastapi_supabase_template/commit/4ee5548fb6d340f7f729f55ae38678817090d578))

* chore: update ci ([`a0f5daa`](https://github.com/Atticuszz/fastapi_supabase_template/commit/a0f5daabdca3cfe93b16db7ab60e499372c6bb69))

* chore: update ci,add changelog as pushed ,Publish to GitHub Releases as test passed and merged from PR ([`eeb3d37`](https://github.com/Atticuszz/fastapi_supabase_template/commit/eeb3d377b51198957b4ab2f4bde0aadd559e9cfc))

* chore: update ci,add changelog as pushed ,Publish to GitHub Releases as test passed and merged from PR ([`f7b2d7e`](https://github.com/Atticuszz/fastapi_supabase_template/commit/f7b2d7e9798ef89a13d7081b7621a6b4b4c02d0c))

### Fix

* fix: failed to yield AsyncClient
feat: add schema.base, add shared methods in CRUD.base for inheriting ,add anyio as async pytest plugin
to fix: CRUDBase create  with wrong url ([`b06fc93`](https://github.com/Atticuszz/fastapi_supabase_template/commit/b06fc936231faa9853f538b60a2d0edb994425be))

### Unknown

* chore：Update pyproject.toml ([`295a2aa`](https://github.com/Atticuszz/fastapi_supabase_template/commit/295a2aac42c3d81d3b7e579f4822bd4b035d50e6))

* Chore：Update ci.yml ([`a405374`](https://github.com/Atticuszz/fastapi_supabase_template/commit/a40537437d5e396fb7dcdca782a9b337a76d2e08))

* Merge pull request #6 from Atticuszz/dependabot/pip/faker-22.2.0

⬆ Bump faker from 22.1.0 to 22.2.0 ([`e1ad025`](https://github.com/Atticuszz/fastapi_supabase_template/commit/e1ad02516a6645758a35910a7b10824fda6b92fe))

* chore：Update ci.yml ([`0ea92f6`](https://github.com/Atticuszz/fastapi_supabase_template/commit/0ea92f6de18b76e50d3f3dbd5abb4c133e81ed7d))

* ⬆ Bump faker from 22.1.0 to 22.2.0

Bumps [faker](https://github.com/joke2k/faker) from 22.1.0 to 22.2.0.
- [Release notes](https://github.com/joke2k/faker/releases)
- [Changelog](https://github.com/joke2k/faker/blob/master/CHANGELOG.md)
- [Commits](https://github.com/joke2k/faker/compare/v22.1.0...v22.2.0)

---
updated-dependencies:
- dependency-name: faker
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a7dd995`](https://github.com/Atticuszz/fastapi_supabase_template/commit/a7dd995097b5e7fdab7eb86ff96a4eb4ed98199b))

* Merge branch &#39;main&#39; of github.com:/Atticuszz/fastapi_supabase_template

# Conflicts:
#	.github/workflows/ci.yml ([`fa0b993`](https://github.com/Atticuszz/fastapi_supabase_template/commit/fa0b99306e116ff25c4f454f158b1a76041e8085))

* Merge pull request #2 from Atticuszz/dependabot/github_actions/codecov/codecov-action-3

⬆ Bump codecov/codecov-action from 1 to 3 ([`2b93b49`](https://github.com/Atticuszz/fastapi_supabase_template/commit/2b93b49bc8a8e4511881a7482ba73bf9e339c762))

* Merge pull request #5 from Atticuszz/dependabot/pip/gitpython-3.1.41

⬆ Bump gitpython from 3.1.40 to 3.1.41 ([`9543321`](https://github.com/Atticuszz/fastapi_supabase_template/commit/95433211bae3a51222c138dd39ff111fc709f254))

* ⬆ Bump gitpython from 3.1.40 to 3.1.41

Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.40 to 3.1.41.
- [Release notes](https://github.com/gitpython-developers/GitPython/releases)
- [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES)
- [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.40...3.1.41)

---
updated-dependencies:
- dependency-name: gitpython
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`783ba60`](https://github.com/Atticuszz/fastapi_supabase_template/commit/783ba60e1ca7763110c9c89f596631a4f4608f96))

* Merge pull request #4 from Atticuszz/dependabot/github_actions/actions/checkout-4

⬆ Bump actions/checkout from 2 to 4 ([`b768155`](https://github.com/Atticuszz/fastapi_supabase_template/commit/b768155e3e53a326a837b96380e1a8b3620a25a2))

* Merge pull request #3 from Atticuszz/dependabot/github_actions/actions/setup-python-5

⬆ Bump actions/setup-python from 2 to 5 ([`d31480b`](https://github.com/Atticuszz/fastapi_supabase_template/commit/d31480b79b7c6571eb6cd9d6acef494fbb88afe3))

* ⬆ Bump actions/checkout from 2 to 4

Bumps [actions/checkout](https://github.com/actions/checkout) from 2 to 4.
- [Release notes](https://github.com/actions/checkout/releases)
- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
- [Commits](https://github.com/actions/checkout/compare/v2...v4)

---
updated-dependencies:
- dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c4dbf9b`](https://github.com/Atticuszz/fastapi_supabase_template/commit/c4dbf9bb530354e7fc3c3835ca2cc091392fd178))

* ⬆ Bump actions/setup-python from 2 to 5

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 2 to 5.
- [Release notes](https://github.com/actions/setup-python/releases)
- [Commits](https://github.com/actions/setup-python/compare/v2...v5)

---
updated-dependencies:
- dependency-name: actions/setup-python
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7653a09`](https://github.com/Atticuszz/fastapi_supabase_template/commit/7653a09f1bbf86f1355b20e4351fa8dd818bc899))

* ⬆ Bump codecov/codecov-action from 1 to 3

Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 1 to 3.
- [Release notes](https://github.com/codecov/codecov-action/releases)
- [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
- [Commits](https://github.com/codecov/codecov-action/compare/v1...v3)

---
updated-dependencies:
- dependency-name: codecov/codecov-action
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8425445`](https://github.com/Atticuszz/fastapi_supabase_template/commit/8425445a98d3f0016f302486a86a8b01ea381851))

* add ci ([`cf8644a`](https://github.com/Atticuszz/fastapi_supabase_template/commit/cf8644aa4a80f2ab48ecb49e4e9f00a64098cee9))

* add ci ([`1d42ded`](https://github.com/Atticuszz/fastapi_supabase_template/commit/1d42ded51b0f09218d13c9940b5d4e5b1c54dfe7))

* removed the auth part ([`d5243b5`](https://github.com/Atticuszz/fastapi_supabase_template/commit/d5243b563a377255d1fa8b79792d013bae583a43))

* Update config.py ([`42c0fe1`](https://github.com/Atticuszz/fastapi_supabase_template/commit/42c0fe1fe1cecd606a81b00e43a46c6387485909))

* Update main.py ([`150a177`](https://github.com/Atticuszz/fastapi_supabase_template/commit/150a1779b7d16ce9a7df4a771473c4100a646f40))

* Update main.py ([`31318df`](https://github.com/Atticuszz/fastapi_supabase_template/commit/31318df05f4340e25fd72cb523f5d1fe2300a5e8))

* Update __init__.py ([`8c5e538`](https://github.com/Atticuszz/fastapi_supabase_template/commit/8c5e53866360d0c9ebbd4606b90114c14be68b6f))

* Update auth.py ([`0bf8050`](https://github.com/Atticuszz/fastapi_supabase_template/commit/0bf80508649eba5327444db52817e5aeeb71d071))

* Update auth.py ([`8f44341`](https://github.com/Atticuszz/fastapi_supabase_template/commit/8f443419e639b59c41aee27f9713bc3d4ddbffc3))

* Update auth.py ([`be89b8b`](https://github.com/Atticuszz/fastapi_supabase_template/commit/be89b8b04304635cec109733f280a4fbf26c7062))

* Update item.py ([`a838580`](https://github.com/Atticuszz/fastapi_supabase_template/commit/a83858080e891b536c391ed4398aec9f34f8a2b1))

* Update item.py ([`5a8f8f4`](https://github.com/Atticuszz/fastapi_supabase_template/commit/5a8f8f4ada8f992fa310f75a1ffec1157716ca7e))

* Update auth.py ([`57d63fe`](https://github.com/Atticuszz/fastapi_supabase_template/commit/57d63fe4791209c74fe9e8e513fccf1d4858eb97))

* finished item,auth ,crud,router ([`46fb284`](https://github.com/Atticuszz/fastapi_supabase_template/commit/46fb284157a4df7a230a01ba4c44361d95bb9c45))

* reshaping ([`f265960`](https://github.com/Atticuszz/fastapi_supabase_template/commit/f2659604fa072363a300163c4c4179dec6a63e41))

* reshaping ([`ca81469`](https://github.com/Atticuszz/fastapi_supabase_template/commit/ca81469f82bb0f8da8a4051f9c9413be4a407860))

* reshaping ([`686d201`](https://github.com/Atticuszz/fastapi_supabase_template/commit/686d2012174dd1a7f3de05d9c468be4df3f203f6))

* reshaping ([`9f6f1e9`](https://github.com/Atticuszz/fastapi_supabase_template/commit/9f6f1e96b005135b3aca4c9b3140e98c8801b1d3))

* Create deps.py ([`faf2489`](https://github.com/Atticuszz/fastapi_supabase_template/commit/faf2489ab1dab412d69f417e15cdcc027205a7ae))

* Create auth.py ([`1c6f384`](https://github.com/Atticuszz/fastapi_supabase_template/commit/1c6f3844ad00970de0e167816f8ee59f5b06854b))

* Delete src/api ([`ad62dbe`](https://github.com/Atticuszz/fastapi_supabase_template/commit/ad62dbe01b8200f9796340f4f9c2ee7cd78aa78f))

* init ([`938a3a6`](https://github.com/Atticuszz/fastapi_supabase_template/commit/938a3a63e9a835b56e86c2fdb40b5511735a985e))

* Initial commit ([`5a6cbfc`](https://github.com/Atticuszz/fastapi_supabase_template/commit/5a6cbfc56fb876239e5b735a8a9b500a1c72597c))
