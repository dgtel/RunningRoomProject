# Output file
$outputFile = "merged_content.txt"

# Backend files
$backendFiles = @(
    "backend\backendapp\urls.py",
    "backend\core\views.py",
    "backend\core\models.py",
    "backend\core\serializers.py"
)

# Frontend files
$frontendFiles = @(
    "RunningRoomFrontend\app\index.tsx",
    "RunningRoomFrontend\app\login.tsx",
    "RunningRoomFrontend\app\admin-dashboard.tsx",
    "RunningRoomFrontend\app\crew-dashboard.tsx",
    "RunningRoomFrontend\app\crew-controller-dashboard.tsx",
    "RunningRoomFrontend\app\care-taker-dashboard.tsx",
    "RunningRoomFrontend\app\contractor-dashboard.tsx",
    "RunningRoomFrontend\app\profile.tsx",
    "RunningRoomFrontend\app\src\config\axiosConfig.ts"
)

# Merge files into one
@(
    # Backend files
    ForEach ($file in $backendFiles) {
        "File: $file"
        Get-Content $file
    }

    # Frontend files
    ForEach ($file in $frontendFiles) {
        "File: $file"
        Get-Content $file
    }
) | Out-File $outputFile

Write-Host "Files merged into $outputFile"
