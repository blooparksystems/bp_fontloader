bp_fontloader
=================

fontloader for speeting up the website
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Thos Fontloader will load the Fonts of the Themes from odoo in the backround.
So that the user see's the text even then the Font isn´t loaded.


.. integration example::


put this in your head of your website

<t t-if="website and website.use_fontloader">
    <script type="text/javascript" src="/your_website/static/src/js/your_website_fontloader.js" />
    <script type="text/javascript" src="/bp_fontloader/static/src/js/fontloader.js"/>
</t>



create a javascript file "your_website_fontloader.js

// bloopark webfont
var WebFontConfig = {
  google: {
    families: [ 'Open+Sans:400,300,600,700','Lato:300,400,700' ]
  },

  timeout: 2000
};


Then delete all fonts form you css files und put them into this js file