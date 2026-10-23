#!/usr/bin/env bash
# 클라우드 세션(Claude 앱 Code 탭, claude.ai/code, 루틴)에서만 커밋 작성자를 noreply로 맞춘다.
# 공개 저장소에 개인 이메일이 남지 않게 하려는 것이다. 로컬(PC)에서는 아무것도 하지 않는다.
[ "$CLAUDE_CODE_REMOTE" = "true" ] || exit 0
cd "$CLAUDE_PROJECT_DIR" || exit 0
git config user.name "taeseob"
git config user.email "taeseob@users.noreply.github.com"
