/**
 * plugins/webfontloader.js
 *
 * webfontloader documentation: https://github.com/typekit/webfontloader
 */

export async function loadFonts () {
  const webFontLoader = await import(/* webpackChunkName: "webfontloader" */'webfontloader')

  webFontLoader.load({
    google: {
      // families: ['Roboto:100,300,400,500,700,900&display=swap'],
      families: ['Poppins:wght@300;600;700&800&family=Rubik:wght@300;400;500&display=swap']
    },
  })
}
