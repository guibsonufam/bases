/* Contas suspeitas
select user.id_str, user.screen_name, user.created_at, text, retweeted_status.user.screen_name
from prolula
where user.id_str='955968218253930497';
*/

/* Usuários com alto degree*/
select created_at, user.id_str, user.screen_name, text, retweeted_status.user.screen_name, retweeted_status.user.id_str, retweet_count, favorite_count
from prolula
where user.id_str='796180188946112512';
