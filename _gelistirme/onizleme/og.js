const { chromium } = require(process.env.PLAYWRIGHT_CORE || 'playwright-core');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args:['--no-sandbox','--allow-file-access-from-files'] });
  const pg = await (await b.newContext({ viewport:{width:1200,height:630}, deviceScaleFactor:1 })).newPage();
  await pg.goto('file://' + process.argv[2], { waitUntil:'load' }); await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(400);
  await pg.screenshot({ path: process.argv[3] }); await b.close();
})();
