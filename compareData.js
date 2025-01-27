const fs = require('fs');
const path = require('path');

const appblogPath = path.join(__dirname, 'appblog');
const appcoderPath = path.join(__dirname, 'appcoder');

function getFiles(dir) {
    let files = [];
    fs.readdirSync(dir).forEach(file => {
        const filePath = path.join(dir, file);
        if (fs.statSync(filePath).isDirectory()) {
            files = files.concat(getFiles(filePath));
        } else {
            files.push(filePath);
        }
    });
    return files;
}

function compareFiles(files1, files2) {
    const set1 = new Set(files1.map(file => path.basename(file)));
    const set2 = new Set(files2.map(file => path.basename(file)));

    const duplicates = [...set1].filter(file => set2.has(file));
    return duplicates;
}

const appblogFiles = getFiles(appblogPath);
const appcoderFiles = getFiles(appcoderPath);

const duplicates = compareFiles(appblogFiles, appcoderFiles);

if (duplicates.length > 0) {
    console.log('Archivos duplicados encontrados:', duplicates);
} else {
    console.log('No se encontraron archivos duplicados.');
}
