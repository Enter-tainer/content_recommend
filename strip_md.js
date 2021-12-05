#!/bin/node
import { remark } from 'remark'
import strip from 'strip-markdown'
import fg from 'fast-glob'
import { toVFile } from 'to-vfile'
import process from 'process'
async function strip_md_files(path) {
  path = path + '/docs/**/*.md'
  const files = fg.stream(path)
  for await (const file of files) {
    console.log(`Stripping ${file}`)
    remark()
      .use(strip)
      .process(await toVFile.read(file))
      .then(async (file) => {
        file.path = file.path + '.stripped'
        await toVFile.write(file)
      })
  }
}

strip_md_files(process.argv[2] || '../OI-Wiki')
