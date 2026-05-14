# Run the Django development server and open it in Google Chrome.
# Usage: Open PowerShell in this folder and run: .\run_chrome_server.ps1

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$activatePaths = @(
    Join-Path $projectRoot "..\myenv\Scripts\Activate.ps1"
    Join-Path $projectRoot "..\venv\Scripts\Activate.ps1"
)

$activateScript = $activatePaths | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $activateScript) {
    Write-Error "Could not find a virtual environment activation script. Checked: $($activatePaths -join ', ')"
    exit 1
}

Write-Host "Activating virtual environment from: $activateScript"
& $activateScript

$url = 'http://127.0.0.1:8000/'
Write-Host "Opening Chrome at $url"
Start-Process chrome $url

Write-Host "Starting Django development server..."
Set-Location $projectRoot
python manage.py runserver
