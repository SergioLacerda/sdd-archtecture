#!/bin/bash
set -e

echo "📦 SDD CLI Build Script"
echo "======================="
echo ""

# Step 1: Install PyInstaller
echo "Step 1: Installing PyInstaller..."
pip install -q pyinstaller

# Step 2: Install requirements
echo "Step 2: Installing CLI dependencies..."
pip install -q -r requirements-cli.txt

# Step 3: Build binary
echo "Step 3: Building standalone binary..."
cd "$(dirname "$0")/.."
pyinstaller build/pyinstaller.spec --distpath ./dist

# Step 4: Verify binary
echo ""
echo "Step 4: Verifying build..."
if [ -f "./dist/sdd" ]; then
    SIZE=$(ls -lh ./dist/sdd | awk '{print $5}')
    echo "✓ Binary created: ./dist/sdd ($SIZE)"
    echo ""
    echo "Binary information:"
    file ./dist/sdd
    ls -lh ./dist/sdd
elif [ -f "./dist/sdd.exe" ]; then
    SIZE=$(ls -lh ./dist/sdd.exe | awk '{print $5}')
    echo "✓ Binary created: ./dist/sdd.exe ($SIZE)"
    echo ""
    echo "Binary information:"
    file ./dist/sdd.exe
    ls -lh ./dist/sdd.exe
else
    echo "✗ Build failed: Binary not found"
    exit 1
fi

echo ""
echo "✓ Build complete! You can now run: ./dist/sdd --help"
