.. _mycred:

mycred plug
==============

Bug fix for mycred plugin in PHP 7.4+
---------------------------------------
In PHP 7.4+, it trigers an error `Notice: Trying to access array offset on value of type bool in ...` when activate extension Rank.

File: mycred/addons/ranks/includes/mycred=rand-functions.php, Line 635 and 656. Change to:

.. code-block:: php

  /**
  * Manual Ranks 
  * @since 1.8
  * @version 1.0
  */
  if ( ! function_exists( 'mycred_manual_ranks' ) ) :
    function mycred_manual_ranks( $point_type = MYCRED_DEFAULT_TYPE_KEY ) {

      $prefs  = mycred_get_addon_settings( 'rank', $point_type );

      $result = false;

       /** to patch for php7.4+ **/
      $tmp = $prefs['base'] ?? 'nothing';

      //if ( $prefs['base'] == 'manual' )
      if ( $tmp == 'manual' )
      /** patch end **/

        $result = true;

      return $result;

    }
  endif;

  /**
  * Rank Based on Total
  * Checks if ranks for a given point type are based on total or current
  * balance.
  * @since 1.6
  * @version 1.1
  */
  if ( ! function_exists( 'mycred_rank_based_on_total' ) ) :
    function mycred_rank_based_on_total( $point_type = MYCRED_DEFAULT_TYPE_KEY ) {

      $prefs  = mycred_get_addon_settings( 'rank', $point_type );

      $result = false;

      /** to patch for php7.4+ **/
      $tmp = $prefs['base'] ?? 'nothing';

      //if ( $prefs['base'] == 'total' )
      if ( $tmp == 'total' )
      /** patch end **/

        $result = true;

      return $result;

    }
  endif;

However, there might be other similar bugs.