import { copyFile, mkdir, readFile, rename, rm } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { join } from 'node:path';

const artwork = new URL('./assets/unzip-the-storm.jpg', import.meta.url);
const outputDirectory = process.env.MAKEFUN_OUTPUT_DIR || '/output';
const expectedHash = '5bab9a3e253e4bdd6b56370927a13d4a3e7bca1862f2ec42a8a48a2b864843ad';
const image = await readFile(artwork);

// Check the exact, fully decoded image inspected during the build.
if (image.length > 1048576 || createHash('sha256').update(image).digest('hex') !== expectedHash) {
  throw new Error('The committed artwork is damaged or exceeds the image size limit.');
}

await mkdir(outputDirectory, { recursive: true });
const output = join(outputDirectory, 'entry.png');
const temporary = join(outputDirectory, `.entry-${process.pid}.tmp`);

// A failed copy leaves the previous complete output intact.
try {
  await copyFile(artwork, temporary);
  const copied = await readFile(temporary);
  if (!copied.equals(image)) {
    throw new Error('The output copy differs from the verified artwork.');
  }
  await rename(temporary, output);
} finally {
  await rm(temporary, { force: true });
}
