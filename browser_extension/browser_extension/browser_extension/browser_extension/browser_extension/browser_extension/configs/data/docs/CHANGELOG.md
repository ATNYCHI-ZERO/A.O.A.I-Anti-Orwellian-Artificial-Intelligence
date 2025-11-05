 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/docs/CHANGELOG.md b/docs/CHANGELOG.md
new file mode 100644
index 0000000000000000000000000000000000000000..0a1de3892b177aec9079aad3747fd0f1932520b6
--- /dev/null
+++ b/docs/CHANGELOG.md
@@ -0,0 +1,7 @@
+# Changelog
+
+## 1.0.0-rc1 — Initial Public-Safe Release
+- Added Constitutional-AI License and compliance documentation.
+- Implemented Local Sovereignty Agent, Truth Engine, Media Shield, and HMAC-SHA256-signed audit ledger with CLI.
+- Shipped Browser Guardian manifest v3 extension.
+- Published investor, legal, branding, and government submission packs.
 
EOF
)
