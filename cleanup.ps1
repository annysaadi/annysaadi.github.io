$filePath = "c:\Users\loany\Documents\annysaadi.github.io\annysaadi.github.io\index.html"
$content = Get-Content -Path $filePath -Raw -Encoding UTF8

# ============================================================
# TASK 1: Fix character encoding
# ============================================================
# The file already has valid UTF-8 Portuguese characters.
# Searching for actual broken Mojibake sequences just in case.
$replacements = [ordered]@{
    'Ã©' = 'é'; 'Ãª' = 'ê'; 'Ã£' = 'ã'; 'Ã§' = 'ç'; 'Ã¡' = 'á'
    'Ã³' = 'ó'; 'Ã­' = 'í'; 'Ãº' = 'ú'; 'Ã‡' = 'Ç'; 'Ã"' = 'Ó'
    'Ã€' = 'À'; 'Ã‰' = 'É'; 'Ã¢' = 'â'; 'Ã´' = 'ô'; 'Ãµ' = 'õ'
    'Ã¼' = 'ü'; 'Ã±' = 'ñ'; 'Ã¥' = 'å'; 'Ã¦' = 'æ'; 'Ã¸' = 'ø'
    'Ã¤' = 'ä'; 'Ã¶' = 'ö'; 'Ã¯' = 'ï'; 'Ã®' = 'î'; 'Ã«' = 'ë'
    'Ã¹' = 'ù'; 'Ã»' = 'û'; 'Ã½' = 'ý'; 'Ã ' = 'à'; 'Ã¨' = 'è'
    'Ã²' = 'ò'; 'Ã‹' = 'Ë'; 'Ãœ' = 'Ü'; 'Ã–' = 'Ö'; 'Ã„' = 'Ä'
}
foreach ($key in $replacements.Keys) {
    $content = $content.Replace($key, $replacements[$key])
}
Write-Host "TASK 1: Encoding replacements applied"

# ============================================================
# TASK 2: Remove modal CSS — MODAL DE INSCRIÇÃO block
# Remove from "      /* MODAL DE INSCRIÇÃO */" through the closing
# of the "@media (max-width: 640px)" block that ends the modal-card styles
# ============================================================

# Remove modal inscription CSS block (lines ~3048-3298)
$content = $content -replace '(?s)\s*/\* MODAL DE INSCRIÇÃO \*/\s*\.modal-overlay \{.*?\}\s*\}\s*/\* MODAL VSL \*/', "`n      /* MODAL VSL */"
Write-Host "TASK 2a: Modal inscription CSS removed"

# Remove VSL modal CSS block (lines ~3299-3540)
# From "/* MODAL VSL */" through the last closing brace of vsl media query
$content = $content -replace '(?s)\s*/\* MODAL VSL \*/\s*\.vsl-overlay \{.*?\.vsl-skip:hover \{[^}]+\}\s*\}\s*@media \(max-width: 640px\) \{[^}]*\.vsl-overlay[^}]*\}\s*[^}]*\.vsl-card[^}]*\}\s*\}', ""
Write-Host "TASK 2b: VSL modal CSS removed"

# ============================================================
# TASK 3: Show hero-kicker — change display:none to display:block
# ============================================================
$content = $content -replace '(\.hero-kicker \{[^}]*?)display:\s*none', '$1display: block'
Write-Host "TASK 3: hero-kicker display:none -> display:block"

# ============================================================
# TASK 5: Move body style blocks to head
# (Do this before removing modal HTML so we don't need to track line shifts)
# ============================================================

# Extract all <style>...</style> blocks from body (after </head>)
$headEndIdx = $content.IndexOf('</head>')
$headPart = $content.Substring(0, $headEndIdx)
$bodyPart = $content.Substring($headEndIdx)

# Collect all style block contents from body
$bodyStyleMatches = [regex]::Matches($bodyPart, '(?s)\s*<style>(.*?)</style>')
$collectedStyles = ""
foreach ($m in $bodyStyleMatches) {
    $collectedStyles += "`n" + $m.Groups[1].Value
}

# Remove all <style>...</style> blocks from body
$bodyPart = [regex]::Replace($bodyPart, '(?s)\s*<style>.*?</style>', '')

# Inject collected styles before closing </style> in head
$headPart = $headPart -replace '(\s*</style>\s*$)', "$collectedStyles`n    </style>"

$content = $headPart + $bodyPart
Write-Host "TASK 5: Body style blocks moved to head"

# ============================================================
# TASK 2 continued: Remove modal HTML elements
# ============================================================

# Remove VSL modal HTML block
$content = $content -replace '(?s)\s*<!-- MODAL VSL -->.*?</div>\s*<!-- MODAL DE INSCRIÇÃO -->', "`n    <!-- MODAL DE INSCRIÇÃO -->"
# Actually remove both modals together
$content = $content -replace '(?s)\s*<!-- MODAL VSL -->.*?</div>\s*\n\s*<!-- MODAL DE INSCRIÇÃO -->.*?</div>\s*\n\s*\n\s*<script>', "`n    <script>"
Write-Host "TASK 2c: Modal HTML blocks removed"

# Remove hero-video-link button with openVSL onclick
$content = $content -replace '(?s)\s*<button class="hero-video-link" type="button" onclick="openVSL\(\)">[^<]*</button>', ''
Write-Host "TASK 2d: openVSL button removed"

# ============================================================
# TASK 2: Remove modal JS functions
# ============================================================

# Remove "// Funções do Modal" block through the modal form validation IIFE and submit handler
# This covers: waNumbers, defaultWaNumber, lastFocusedElement, focusableSelector, helper functions,
# trapFocus, openModal, closeModal, closeModalOnOverlay, modal form setup IIFE, modalForm submit listener
$content = $content -replace '(?s)\s*// Funções do Modal\s*const waNumbers.*?closeModalOnOverlay\(event\);\s*\}\s*\}\s*\)', ""
Write-Host "TASK 2e: Modal JS helper functions removed"

# Remove modalForm event listener block
$content = $content -replace '(?s)\s*// Envio do formulário do modal.*?modal\.classList\.add\("open"\);\s*\}\s*// Fechar modal com tecla ESC', "`n      // Fechar modal com tecla ESC"
Write-Host "TASK 2f: Modal form submission JS removed"

# Update keydown handler to remove modal references
$content = $content -replace '(?s)(// Fechar modal com tecla ESC\s*document\.addEventListener\("keydown", function \(event\) \{)\s*const openSignupModal.*?if \(openVslModal\) trapFocus\(event, openVslModal\);\s*\}\)', @'
      // Fechar modal com tecla ESC
      document.addEventListener("keydown", function (event) {
        const openVslModal = document.querySelector(
          "#vslModal.vsl-active .vsl-card",
        );

        if (event.key === "Escape") {
          if (openVslModal) closeVSL();
          return;
        }

        if (openVslModal) trapFocus(event, openVslModal);
      });
'@
Write-Host "TASK 2g: Keydown handler updated"

# Remove openModal GA tracking reassignment at bottom
$content = $content -replace '(?s)\s*// Track abertura do modal\s*const originalOpenModal = openModal;\s*openModal = function \(\) \{[^}]+\};\s*</script>', "`n    </script>"
Write-Host "TASK 2h: Modal GA tracking removed"

# Remove VSL modal JS block (last <script> tag)
$content = $content -replace '(?s)\s*<script>\s*// VSL Modal\s*function closeVSL\(\).*?}\s*</script>\s*</body>', "`n  </body>"
Write-Host "TASK 2i: VSL modal JS block removed"

# ============================================================
# Write the final file
# ============================================================
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
Write-Host "File written successfully"
