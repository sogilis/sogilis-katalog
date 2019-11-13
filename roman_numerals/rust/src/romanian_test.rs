#[cfg(test)]
mod romanian_test {
    use super::super::romanian_count;

    #[test]
    fn translate_romanian() {
        assert_eq!(romanian_count(&String::from("")), 0);
        assert_eq!(romanian_count(&String::from("I")), 1);
        assert_eq!(romanian_count(&String::from("II")), 2);
        assert_eq!(romanian_count(&String::from("III")), 3);
    }
}
